import React from 'react';
import type { ItemListElements } from 'src/types';
import { JsonLdProps } from './jsonld';
export interface BreadCrumbJsonLdProps extends JsonLdProps {
    itemListElements: ItemListElements[];
}
declare function BreadCrumbJsonLd({ type, keyOverride, itemListElements, ...rest }: BreadCrumbJsonLdProps): React.JSX.Element;
export default BreadCrumbJsonLd;
