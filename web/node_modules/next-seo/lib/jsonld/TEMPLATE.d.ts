import React from 'react';
import { JsonLdProps } from './jsonld';
export interface HEREJsonLdProps extends JsonLdProps {
}
declare function HEREJsonLd({ type, keyOverride, ...rest }: HEREJsonLdProps): React.JSX.Element;
export default HEREJsonLd;
