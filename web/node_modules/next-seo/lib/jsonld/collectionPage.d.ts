import React from 'react';
import { JsonLdProps } from './jsonld';
import type { CreativeWork } from 'src/types';
export interface CollectionPageJsonLdProps extends JsonLdProps {
    name: string;
    hasPart: CreativeWork[];
}
declare function CollectionPageJsonLd({ type, keyOverride, hasPart, ...rest }: CollectionPageJsonLdProps): React.JSX.Element;
export default CollectionPageJsonLd;
